import shutil
import os

_product_version="2.3.0"
_image_remote="quay.io/nathanweatherly"
_hub_mock_component_image_sha="9c5cf5335d7a948bed2f69f1e41f407f62820f996ad3368d5aed5183bcc41008"

_git_repo_base_dir = os.getcwd() # base repo directory
_templates_dir = os.path.join(_git_repo_base_dir, "templates")
_template_image_man_file_path = os.path.join(_templates_dir, "template-image-manifest.json")
_results_dir = os.path.join(_git_repo_base_dir, "results")

if not os.path.isdir(_results_dir):
    os.mkdir(_results_dir)

_new_image_man_destination = os.path.join(_results_dir, "{}.json".format(_product_version))
_new_image_man_path= shutil.copy(_template_image_man_file_path, _new_image_man_destination)

with open(_new_image_man_path) as f:
    _image_man_text=f.read()
    _image_man_text= _image_man_text.replace('HUB_MOCK_COMPONENT_IMAGE_SHA', _hub_mock_component_image_sha)
    _image_man_text= _image_man_text.replace('IMAGE_REMOTE', _image_remote)

with open(_new_image_man_path, "w") as f:
    f.write(_image_man_text)