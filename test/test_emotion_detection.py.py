import unittest
from .. import emotion_detection

emotion_detection("Hi, I feel great!")

class TestMyModule(unittest.TestCase):
    def test_emotion_detection(self):
        self.assertEqual(emotion_detection("I am glad this happened"), "Joy")
        self.assertEqual(emotion_detection("I am really mad about this"), "anger")
        self.assertEqual(emotion_detection("I feel disgusted just hearing about this"), "disgust")
        self.assertEqual(emotion_detection("I am so sad about this"), "sadness")
        self.assertEqual(emotion_detection("I am really afraid that this will happen"), "fear")

if __name__ == "__main__":
    unittest.main()