<!--next-version-placeholder-->

## v0.7.0 (2023-11-07)

### Feature

* **autotrain:** Add test script for AutoModelForCausalLM ([`bde4cbe`](https://github.com/chu-aie/deepnlp-2023/commit/bde4cbe5a161e06690ed0ade7366e4deb5d080eb))
* **examples/autotrain:** Add README.md for fine-tuning Large Language Models with Hugging Face's AutoTrain ([`374db46`](https://github.com/chu-aie/deepnlp-2023/commit/374db460e4a186df6d41a32b349d95f8d41a38ae))
* **autotrain:** Add DATA_FILE parameter ([`4cf03a1`](https://github.com/chu-aie/deepnlp-2023/commit/4cf03a14b6f74a2bac3cdf1d66bf586a2bb1eda6))
* **autotrain:** Add data_file environment variable ([`583380b`](https://github.com/chu-aie/deepnlp-2023/commit/583380b273401e24f935b79dc911e3872c6ddd73))
* **autotrain:** Add dataload.py for loading the dataset ([`5a16671`](https://github.com/chu-aie/deepnlp-2023/commit/5a166713feac4c6ebeb5ce2e253bd89018a220ad))
* **autotrain:** Add new falcon environment configuration file ([`febce8e`](https://github.com/chu-aie/deepnlp-2023/commit/febce8e3845da0006527dac424e761164963f56a))
* **autotrain:** Add new script for automated training ([`87c417e`](https://github.com/chu-aie/deepnlp-2023/commit/87c417ec125f804fd4b1a4e8601caf709dd546db))
* **Dockerfile.app:** Install Git LFS for large file version control ([`bdc25c3`](https://github.com/chu-aie/deepnlp-2023/commit/bdc25c31515b8f5710f016754f3bfa0904d887e1))
* **Dockerfile.base:** Add ffmpeg and related libraries to Dockerfile ([`bfd73a6`](https://github.com/chu-aie/deepnlp-2023/commit/bfd73a6e9bf856495c082da55da37949bf397238))
* **docker:** Add git-lfs to Dockerfile.base ([`779a219`](https://github.com/chu-aie/deepnlp-2023/commit/779a2191ad3b7b54a2c835ec04dceefa53de0187))
* **autotrain:** Add requirements.txt ([`9ebb1d2`](https://github.com/chu-aie/deepnlp-2023/commit/9ebb1d2dd1efeb74162c06217c4bf000e217193c))

### Fix

* **autotrain:** Change data-path to root ([`ab20acb`](https://github.com/chu-aie/deepnlp-2023/commit/ab20acb27f327e7f0ade10c08d6518f385fac85d))
* **autotrain:** Replace DATA_PATH with DATA_FILE ([`04556a6`](https://github.com/chu-aie/deepnlp-2023/commit/04556a653344524e0c5115efb89362c85623a31e))

## v0.6.0 (2023-10-31)

### Feature

* **docker-compose:** Add exec command, add workspace directories creation ([`980b29e`](https://github.com/chu-aie/deepnlp-2023/commit/980b29e0c83481a2529dd74fc91abf42972d2934))
* **ollama:** Add docker-compose.yaml file, add docker.env file ([`03acea4`](https://github.com/chu-aie/deepnlp-2023/commit/03acea46f92833f0c636258442c6875860204822))
* **mistral:** Add model download script ([`3fffc00`](https://github.com/chu-aie/deepnlp-2023/commit/3fffc001a312285670a63c380e6d20ac81f3d08a))
* **mistral:** Add model name and huggingface paths to docker environment variables. ([`127cf2e`](https://github.com/chu-aie/deepnlp-2023/commit/127cf2ec60c9ea26f669db1152097d96d8fc742c))
* **docs:** Add Quickstart guide for Mistral AI ([`b340a7a`](https://github.com/chu-aie/deepnlp-2023/commit/b340a7a0d0a2bbded176c005373d522031a8676f))
* **docker:** Add docker.common.env configuration file ([`3a2047b`](https://github.com/chu-aie/deepnlp-2023/commit/3a2047b4e0de47369515e3ef7aa8db53bf449272))
* **docker:** Add new docker configuration for Mistral project ([`b119452`](https://github.com/chu-aie/deepnlp-2023/commit/b11945252317701de465ca09109b604800244d2a))
* **llmsvc/mistral:** Add docker-compose.yaml configuration ([`5e4bf42`](https://github.com/chu-aie/deepnlp-2023/commit/5e4bf42a23450c92d1f8d0af73d5eaf16c48a7a8))
* **docker-compose:** Add new docker-compose script ([`2ee1ce6`](https://github.com/chu-aie/deepnlp-2023/commit/2ee1ce64280bbe6037c28f641b21f4b30b00c870))

## v0.5.0 (2023-10-29)

### Feature

* **agent_output:** Add new file scrape_speeches.py for speech scraping functionality ([`2c2ebb0`](https://github.com/chu-aie/deepnlp-2023/commit/2c2ebb043d8a6548fdd3cb6e8781a73a7e08ecf9))
* **autogen:** Add requirements.txt with dependencies ([`de49167`](https://github.com/chu-aie/deepnlp-2023/commit/de4916724e5a655b74eccc608919c03a52eacdbd))
* **autogen:** Add new AssistantAgent and UserProxyAgent in autoscraper.py ([`9f2b677`](https://github.com/chu-aie/deepnlp-2023/commit/9f2b677b79014a8337efab2bb1877ba041023d17))
* **Makefile:** Add ollama container commands ([`8300c0d`](https://github.com/chu-aie/deepnlp-2023/commit/8300c0d0b995f01927b341736d2021b8f99ff33b))
* **ollama:** Add new environment variables ([`bbb2075`](https://github.com/chu-aie/deepnlp-2023/commit/bbb2075a338c9af77cfe324d8c6fdc4c8ec0c9e2))
* **ollama:** Add script for docker operations ([`d527309`](https://github.com/chu-aie/deepnlp-2023/commit/d527309d7ecab7b726180bcf5169ae067dd0d423))
* **ollama:** Add README.md for tool usage instructions ([`4afad8e`](https://github.com/chu-aie/deepnlp-2023/commit/4afad8e2cef5d682253d8b91a6e827dd50e0489a))

### Fix

* **dependencies:** Adjust python version constraint ([`1a0532a`](https://github.com/chu-aie/deepnlp-2023/commit/1a0532a7da0ca82cbac7b42a96c62834a70b4aec))

## v0.4.0 (2023-10-21)

### Feature

* **docker-scripts:** Add sshd_config file and copy sshd_config to appropriate directory ([`7c38c74`](https://github.com/chu-aie/deepnlp-2023/commit/7c38c746880edbaf4a5dece30f988660706cdeb7))
* **Dockerfile.base:** Add zsh to the list of packages installed ([`aebbfc0`](https://github.com/chu-aie/deepnlp-2023/commit/aebbfc07ea88ff537db76e444ad3e03d5c93b955))
* **docker:** Add new project environment files ([`e455642`](https://github.com/chu-aie/deepnlp-2023/commit/e455642a0792c2ef9e62100f105587c6f4cd626f))
* **docker:** Add admin.env configuration for Docker ([`a6af5d6`](https://github.com/chu-aie/deepnlp-2023/commit/a6af5d6d265eb524bd96617e847c67961e7ca4bc))
* **docker:** Add jupyterlab to base requirements ([`8565712`](https://github.com/chu-aie/deepnlp-2023/commit/856571239cbe43023fd5bc88ecd4c244dd75c6ad))
* **docker:** Add container ID support ([`6cbf058`](https://github.com/chu-aie/deepnlp-2023/commit/6cbf058c7bb82c1fece557468059eea7067d47d6))
* **pyproject.toml:** Add version_pattern in semantic_release ([`1cd1e25`](https://github.com/chu-aie/deepnlp-2023/commit/1cd1e25c9e9b5e7a8d2bcffbf97590a37aa3c4c8))
* **docker-config:** Add new docker configuration file ([`43e08f2`](https://github.com/chu-aie/deepnlp-2023/commit/43e08f2a934cd55bf4681400983aac290a36af8b))

## v0.3.0 (2023-09-17)

### Feature

* **projects:** Add proposal template ([`7b0466f`](https://github.com/chu-aie/deepnlp-2023/commit/7b0466f722af9eabc043ef3b1a75315950d0a0bd))

## v0.2.0 (2023-08-27)

### Feature

* **id:** Add README.md ([`a4b6959`](https://github.com/chu-aie/deepnlp-2023/commit/a4b6959cc0c9bab92f634fea462096e47b764836))
* **syllabus:** Add new course syllabus content ([`aaceeab`](https://github.com/chu-aie/deepnlp-2023/commit/aaceeab27a7f59885b1769f86f339572650300cd))
* **book:** Add new project details ([`dd9c108`](https://github.com/chu-aie/deepnlp-2023/commit/dd9c1088010afb670c576cedca3fa1bad787f44a))
* **book:** Add projects index page ([`8610507`](https://github.com/chu-aie/deepnlp-2023/commit/8610507b39cbff7b4a7f1e34a666c1e4e1b9aefc))
* **.github/workflows:** Add toc file generation step ([`f8bdd35`](https://github.com/chu-aie/deepnlp-2023/commit/f8bdd3508fb01717f0c16a8e68dd605ed871abd8))
* **scripts:** Add autotoc.py for TOC generation ([`76958b8`](https://github.com/chu-aie/deepnlp-2023/commit/76958b80464a4da80b17bd7876c62b380c256db4))
* **tasks:** Add table of contents generation task ([`223f55b`](https://github.com/chu-aie/deepnlp-2023/commit/223f55bacd8d8d84b8dcb02a04de71a77624c103))

### Documentation

* **README:** Add course syllabus and lecture notes links ([`b840720`](https://github.com/chu-aie/deepnlp-2023/commit/b8407202662b075b285ed9e26ad126fc94d75f77))
* **README:** Add course and lecture badges ([`5475507`](https://github.com/chu-aie/deepnlp-2023/commit/5475507b57cd79d2bca40152d9d7cfa6f2e6efe2))

## v0.1.0 (2023-08-25)

### Feature

* Initial version ([`bdfe58d`](https://github.com/chu-aie/deepnlp-2023/commit/bdfe58d45112ea732de5990629196f11ee728ec4))
