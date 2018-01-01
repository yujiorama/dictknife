from ._lazyimport import m


def load(fp, *, loader=None, **kwargs):
    return m.yaml.load(fp, Loader=m.yaml.Loader, **kwargs)


def dump(d, fp, *, sort_keys=False):
    dumper_class = m.yaml.SortedDumper if sort_keys else m.yaml.Dumper
    return m.yaml.dump(d, fp, allow_unicode=True, default_flow_style=False, Dumper=dumper_class)
