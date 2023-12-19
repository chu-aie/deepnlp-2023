#!/bin/bash
# add your custom commands here that should be executed when building the docker image
# arguments usage
USAGE="
$0 COMMAND [OPTIONS]

Arguments:
COMMAND                The operation to be performed. Must be one of: [data|train|test]

Options:
-m, --model MODEL_NAME          Specify a MODEL_NAME to finetune for test or train. (Name of .env file without extension)
-p, --pid PROJECT_ID            Specify a project ID to diffrentiate runs.
-h, --help                      Display this help message.

Example:
$0 train -m falcon
"

# declare arguments
PROJECT_ID="admin"
COMMAND="train"
MODEL_NAME="mymodel"
ADDITIONAL_ARGS=""

set +u
# read arguments
# first argument is the command
COMMAND="$1"
shift

# parse options
while [[ $# -gt 0 ]]; do
    case "$1" in
    -m | --model)
        MODEL_NAME="$2"
        shift
        ;;
    --model=*)
        MODEL_NAME="${1#*=}"
        ;;
    -p | --pid)
        PROJECT_ID="$2"
        shift
        ;;
    --pid=*)
        PROJECT_ID="${1#*=}"
        ;;
    -h | --help)
        echo "Usage: $0 $USAGE" >&2
        exit 0
        ;;
    -h*)
        echo "Usage: $0 $USAGE" >&2
        exit 0
        ;;
    *)
        ADDITIONAL_ARGS="$ADDITIONAL_ARGS $1"
        ;;
    esac
    shift
done
# check if remaining arguments exist
if [[ -n "$ADDITIONAL_ARGS" ]]; then
    echo "Additional arguments: $ADDITIONAL_ARGS" >&2
fi
set -u

if [ "${COMMAND}" == "data" ]; then
    echo "Preparing data for MODEL_NAME: ${MODEL_NAME}"
elif [ "${COMMAND}" == "train" ]; then
    echo "Autotrain for MODEL_NAME: ${MODEL_NAME}"
elif [ "${COMMAND}" == "test" ]; then
    echo "Test for MODEL_NAME: ${MODEL_NAME}"
else
    echo "Invalid command: $COMMAND" >&2
    echo "Usage: $0 $USAGE" >&2
    exit 1
fi
echo "---"

# load environment variables and print them
export PROJECT_ID="${PROJECT_ID}"
set -a
MODEL_ENV_FILE="${MODEL_NAME}.env"
if [ -e "${MODEL_ENV_FILE}" ]; then
    echo "Loading model specific environment variables from ${MODEL_ENV_FILE}"
    set -x # print commands and thier arguments
    # shellcheck disable=SC1091,SC1090
    source "${MODEL_ENV_FILE}"
    set +x # disable printing of environment variables
fi
set +a

# run docker-compose
if [ "${COMMAND}" == "data" ]; then
    CMD="python3 dataload.py"
elif [ "${COMMAND}" == "train" ]; then
    CMD="autotrain llm \
            --train \
            --model ${MODEL_NAME} \
            --project-name ${AUTOTRAIN_PROJECT_NAME} \
            --data-path ${DATA_PATH} \
            --lr ${LEARNING_RATE} \
            --batch-size ${BATCH_SIZE} \
            --epochs ${NUM_EPOCHS} \
            --block-size ${BLOCK_SIZE} \
            --warmup-ratio ${WARMUP_RATIO} \
            --lora-r ${LORA_R} \
            --lora-alpha ${LORA_ALPHA} \
            --lora-dropout ${LORA_DROPOUT} \
            --weight-decay ${WEIGHT_DECAY} \
            --gradient-accumulation ${GRADIENT_ACCUMULATION}"

    [[ -n "$TEXT_COLUMM" ]] && CMD="$CMD --text-column $TEXT_COLUMM}"
    [[ "$USE_FP16" == "True" ]] && CMD="$CMD --fp16"
    [[ "$USE_PEFT" == "True" ]] && CMD="$CMD --use-peft"
    [[ "$USE_INT4" == "True" ]] && CMD="$CMD --use-int4"
    [[ "$PUSH_TO_HUB" == "True" ]] && CMD="$CMD --push-to-hub --token ${HF_TOKEN} --repo-id ${REPO_ID}"

elif [ "${COMMAND}" == "test" ]; then
    CMD="python3 test.py"
fi
echo "Running command: ${CMD}"
eval "${CMD}"
