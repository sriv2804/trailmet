from .resnet import get_resnet_model


class ModelsFactory(object):
    @staticmethod
    def create_model(**kwargs):
        """
        Returns the requested model, ready for training/pruning with the specified method

        Args:
            name: model name 'resnet18','resnet50'
            num_classes: number of classes
        Return:
            model object
        """
        assert 'name' in kwargs, "should provide model name"
        assert 'num_classes' in kwargs, "should provide number of classes"
        name = kwargs['name']
        num_classes = kwargs['num_classes']

        if 'resnet' in name:
            assert 'insize' in kwargs, "should provide input size"
            insize = kwargs['insize']
            model = get_resnet_model(name, num_classes, insize)
        else:
            raise Exception("unknown model {}".format(kwargs['name']))
        return model