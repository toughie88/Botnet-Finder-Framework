
import json

from unittest import TestCase
from datasets import DatasetBuilder
from extractors import Extractor


class TestDisclosureExtractor(TestCase):
    def test_extract(self):
        with open('test_disclosureExtractor_DatasetBuilder_config.json') as f:
            dataset_builder_config = json.load(f)

        dataset = DatasetBuilder('disclosure').build('test_disclosureExtractor.csv', **dataset_builder_config)

        with open('test_disclosureExtractor_Extractor_config.json') as f:
            extractor_config = json.load(f)

        features = Extractor('disclosure').extract(dataset, **extractor_config)

        with open('test_disclosureExtractor_features.json') as f:
            oracle = json.load(f)

        for server in features:
            for feature in features[server]:
                if feature != 'label':
                    self.assertAlmostEqual(features[server][feature], oracle[server][feature], msg='server: ' + server + ', feature: ' + feature + ' := ' + str(features[server][feature]) + ' != ' + str(oracle[server][feature]))

    def __init__(self, *args, **kwargs):
        super(TestDisclosureExtractor, self).__init__(*args, **kwargs)
