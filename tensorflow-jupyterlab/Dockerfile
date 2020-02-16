ARG BASE_CONTAINER=jupyter/scipy-notebook
FROM $BASE_CONTAINER


RUN conda upgrade --quiet --yes \
    'notebook' \
    'jupyterhub' \
    'jupyterlab' && \
    conda clean --all -y && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

RUN conda install --quiet --yes \
    'tensorflow=2.*' \
    'graphviz' \
    'keras=2.*' && \
    conda clean --all -y && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

RUN jupyter labextension install @ryantam626/jupyterlab_code_formatter

RUN pip install --upgrade pip && \
    pip install jupyterlab_code_formatter && \
    pip install black && \
    pip install Tensorboard && \
    pip install pydotplus && \
    pip install graphviz && \
    npm cache clean --force && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn

RUN jupyter serverextension enable --py jupyterlab_code_formatter

COPY --chown=$NB_UID ./shortcuts.jupyterlab-settings /home/jovyan/.jupyter/lab/user-settings/\@jupyterlab/shortcuts-extension/shortcuts.jupyterlab-settings
