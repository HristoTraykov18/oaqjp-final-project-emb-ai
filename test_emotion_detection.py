import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        test_input = (
            'I am glad this happened',
            'I am really mad about this',
            'I feel disgusted just hearing about this',
            'I am so sad about this',
            'I am really afraid that this will happen'
        )
        expected_output = ('joy', 'anger', 'disgust', 'sadness', 'fear')

        for i in range(0, len(test_input)):
            self.assertEqual(emotion_detector(test_input[i])[
                             'dominant_emotion'], expected_output[i])


if __name__ == '__main__':
    unittest.main()
