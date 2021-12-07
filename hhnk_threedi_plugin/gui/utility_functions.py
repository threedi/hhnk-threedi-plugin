def get_revision(text_in):
    """Retrieve revision from model result. This only works when the revision
    is in the model result with a # followed by a space. e.g. '#12 '
    """
    # TODO Moet deze functie ergens anders heen?
    try:
        return text_in.split("#")[1].split(" ")[0].split("_")[0].zfill(2)
    except Exception as e:
        return 0
