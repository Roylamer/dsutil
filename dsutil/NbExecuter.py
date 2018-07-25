from nbparameterise import extract_parameters, parameter_values, replace_definitions
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat
import os
import io


def execute_nb(path, execute_dte):
    # Reset python workspace
    chdir = '/'.join(os.path.abspath(path).split('/')[:-1])
    os.chdir(chdir)


    # Execute notebook
    with io.open(path, mode="r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    orig_parameters = extract_parameters(nb)


    # Update the parameters and run the notebook
    params = parameter_values(orig_parameters, execute_dte=execute_dte)
    new_nb = replace_definitions(nb, params)

    # Save results back to the notebook
    with io.open(path, mode="w", encoding="utf-8") as f:
        nbformat.write(new_nb, f)


def execute_nb2(path, **kwargs):
    # Reset python workspace
    chdir = '/'.join(os.path.abspath(path).split('/')[:-1])
    os.chdir(chdir)

    # Execute notebook
    with io.open(path, mode="r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    orig_parameters = extract_parameters(nb)

    # Update the parameters and run the notebook
    execution_date = '2018-01-01'
    signature = {'dag_id':'', 'task_id':'', 'owner':'', 'nb_path':path, 'execution_date': execution_date}
    try:
        execution_date=kwargs.get('execution_date', '').strftime('%Y-%m-%d')
        signature['dag_id'] = str(kwargs.get('dag').dag_id)
        signature['task_id'] = str(kwargs.get('task').task_id)
        signature['owner'] = str(kwargs.get('task').owner)
        signature['execution_date'] = execution_date
    except:
        pass
    params = parameter_values(orig_parameters, 
                              execution_date=execution_date,
                              signature=str(signature)
                             )
    new_nb = replace_definitions(nb, params)

    # Save results back to the notebook
    with io.open(path, mode="w", encoding="utf-8") as f:
        nbformat.write(new_nb, f)

        
def execute_r(path, **kwargs):
    # read the notebook
    with open(path) as f:
        nb = nbformat.read(f, as_version=4)
        
    # execute the notebook
    ep = ExecutePreprocessor(timeout=-1)
    ep.preprocess(nb, {'metadata': {}})
    
    # write the notebook
    with open(path, 'wt') as f:
        nbformat.write(nb, f)
        
        
        