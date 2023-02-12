import boto3
import sys
import click


@click.group()
def cli():
    """Commands for all cli"""
