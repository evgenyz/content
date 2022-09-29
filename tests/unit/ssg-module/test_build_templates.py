import os
import pytest

import ssg.templates as tpl
from ssg.environment import open_environment
import ssg.utils
import ssg.products
from ssg.yaml import ordered_load, open_raw
import ssg.build_yaml
import ssg.build_cpe


ssg_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
DATADIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))
templates_dir = os.path.join(DATADIR, "templates")
remediations_dir = os.path.join(DATADIR, "remediations")
checks_dir = os.path.join(DATADIR, "checks")
platforms_dir = os.path.join(DATADIR, "platforms")

build_config_yaml = os.path.join(ssg_root, "build", "build_config.yml")
product_yaml = os.path.join(ssg_root, "products", "rhel8", "product.yml")
env_yaml = open_environment(build_config_yaml, product_yaml)


"""
@pytest.fixture
def env_yaml():
    env_yaml = dict(product="rhel7")
    return env_yaml

@pytest.fixture
def product_cpes():
    product_yaml_path = os.path.join(DATADIR, "product.yml")
    product_yaml = open_raw(product_yaml_path)
    product_yaml["product_dir"] = os.path.dirname(product_yaml_path)
    product_cpes = ssg.build_cpe.ProductCPEs()
    product_cpes.load_product_cpes(product_yaml)
    product_cpes.load_content_cpes(product_yaml)
    return product_cpes

@pytest.fixture
def cpe_platforms(env_yaml, product_cpes):
    platforms = dict()
    platform_path = os.path.join(DATADIR, "machine.yml")
    platform = ssg.build_yaml.Platform.from_yaml(platform_path, env_yaml, product_cpes)
    platforms[platform.name] = platform
    return platforms
"""


def test_build_platforms():
    builder = ssg.templates.Builder(
        env_yaml, '', templates_dir,
        remediations_dir, checks_dir, platforms_dir)

    builder.build_all_platforms()


def xtest_build_lang_file_oval():
    builder = ssg.templates.Builder(
        env_yaml, '', templates_dir,
        remediations_dir, checks_dir, platforms_dir)

    text = builder.build_lang_file('rule_id', 'cond_arch', {'arg': 'Argument'}, 'oval', env_yaml)

    assert 'Architecture is Argument' in text
