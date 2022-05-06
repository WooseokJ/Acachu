#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # # 카페 태그 모델 (BERT) Load :
    # save_path = os.getcwd() + '\\nlp\\bert_clf_v2'
    # tags_model = tf.saved_model.load(save_path)

    # # 긍부정 분류 모델 (BiLSTM) Load :
    # train = np.load(os.getcwd()+'\\nlp\\x_train_okt_V3.npy', allow_pickle=True)
    # sentiment_model = load_model(os.getcwd()+'\\nlp\\bilstm_okt_v3.h5')
    main()

