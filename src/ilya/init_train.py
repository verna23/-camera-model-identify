
from pipeline import config
from pipeline.core.train_core import train_model


def main():
    print('Training total of {} models'.format(len(config.MODELS)))
    for i, model_name in enumerate(config.MODELS):
        print('{}/{}: Training {} (logging to src/ilya/logs/{})'.format(
            i + 1, len(config.MODELS), model_name, model_name)
        )
        train_model(model_name, use_pseudo=False)


if __name__ == '__main__':
    main()
