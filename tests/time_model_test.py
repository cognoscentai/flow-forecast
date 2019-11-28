from flood_forecast.model_dict_function import pytorch_model_dict as pytorch_model_dict1
import unittest
import os

class TimeSeriesModelTest(unittest.TestCase):
    def setUp(self):
        self.test_path = ""

    def test_pytorch_model_dict(self):
        self.assertEqual(type(pytorch_model_dict1), dict)

    def test_pytorch_wrapper_default(self):
        model_params = {"number_time_series":3}
        model = PyTorchForecast("MultiAttnHeadSimple", "", "", "", model_params)
        self.assertEqual(model.model.dense_shape.in_features, 3)
        self.assertEqual(model.model.multi_attn.embed_dim, 128)

    def test_pytorch_wrapper_custom(self):
        model_params = {"number_time_series":6, "d_model":112}
        model = PyTorchForecast("MultiAttnHeadSimple", "", "", "", model_params)
        self.assertEqual(model.model.dense_shape.in_features, 6)
        self.assertEqual(model.model.multi_attn.embed_dim, 112)
if __name__ == '__main__':
    unittest.main()