# Cartogram Serverless

This repository contains Python code to allow the cartogram generator to be called in an AWS Lambda function. The lambda function code can be found in `lambda_package/lambda_function.py`.

If you encounter any issues, or have any questions, please contact Ian Duncan at ian.duncan@u.yale-nus.edu.sg.

## Setting Up Local Development

This repository comes with some helper scripts to simulate the AWS Lambda environment on your machine. This allows you to test changes to the Lambda function code locally, and to run the new serverless cartogram web application locally. There are only a few steps you need to follow to set up local development.

First, make sure you have Python, PIP, and Virtualenv installed. On Mac OS, you can install these dependencies using Homebrew:

```
$ brew install python3
$ pip3 install virtualenv
```

On Ubuntu, there are binary packages available:

```
$ sudo apt-get install python3 python3-pip
$ sudo pip3 -H install virtualenv
```

Then, copy `envsettings.sh.dist` to `envsettings.sh`. You should change the environment variables from their default settings as needed, but you shouldn't need to make too many changes:

`LAMBDA_FUNCTION_NAME`: When you deploy, your Lambda function code will be uploaded to the Lambda function with this namme.

`CARTOGRAM_PROGRESS_URL`: The Lambda function sends progress information during cartogram generation to the cartogram web application to this URL. If you have configured the cartogram web application to run locally at `localhost:5000` (the default), you don't need to change this.

`CARTOGRAM_PROGRESS_SECRET`: When the Lambda function sends progress information, it includes this string to authenticate itself to the cartogram web application. You can leave this empty for local development.

`LAMBDA_TASK_ROOT`: The Lambda function expects this environment variable to point to the folder where the Lambda function code is stored. Do not change this.

`LAMBDA_SIMULATOR_HOST`, `LAMBDA_SIMULATOR_PORT`: By default, the Lambda function simulator will make an HTTP interface to the Lambda function available at `localhost:5050`. You shouldn't need to change this.

Next, you can install the Python software dependencies and ensure that the Python virtual environment is working:

```
$ source ./setupenv_local.sh
```

When this command is finished running, your command prompt should change to indicate you are inside the virtual environment:

```
(venv-local) $
```

**If you are not using Linux,** you must also provide a working binary for the cartogram generator for your system. If you haven't already, compile the C code for the cartogram generator at https://github.com/mgastner/cartogram. Inside this repository, the cartogram generator binary will be located at `cartogram_generator/cartogram`. First, back up the Linux binary provided in this repository, and install your version:

```
$ mv lambda_package/cartogram lambda_package/cartogram-linux
$ cp /path/to/cartogram/repository/cartogram_generator/cartogram lambda_package/cartogram
```

## Running the Lambda Simulator

Once you have set up the code for local development, you can run the Lambda Simulator. This is a small Python script that simulates the Amazon Lambda and Gateway API features used by the Lambda function and cartogram web application so you can test both locally. You can start the Lambda simulator with the following commands:

```
$ source ./setupenv_local.sh
(venv-local) $ python simulate_lambda.py
```

When you are finished, simply press `CTRL-C` in the terminal window to kill the Lambda Simulator process.

## Deploying Your Changes

This repository contains scripts to deploy your code changes to the live AWS Lambda function. Before you can deploy, you must set up the [AWS CLI](https://docs.aws.amazon.com/comprehend/latest/dg/setup-awscli.html).

**If you are not using Linux,** you must restore your backed-up Linux cartogram generator binary before deploying:

```
$ mv lambda_package/cartogram lambda_package/cartogram-local
$ mv lambda_package/cartogram-linux lambda_package/cartogram
```

Now, run the deploy script:

```
$ source ./setupenv_local.sh
$ ./deploy.sh
```

If you receive the message `ERROR: lambda_package/cartogram is not a Linux executable.`, then you have likely not restored the backed-up Linux cartogram generator binary. Please follow the instructions above.

**If you are not using Linux,** you can restore your local cartogram generator binary after you're finished deploying:

```
$ mv lambda_package/cartogram lambda_package/cartogram-linux
$ mv lambda_package/cartogram-local lambda_package/cartogram
```
