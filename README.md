# ec2-autostop
Stop EC2 Instances in my Account Automatically, to avoid runaway costs when I forget.

This cleans up any instances in the region I usually use (eu-west-1)

Only instances tagged with a Tag "KeepRunning" do not get stopped.

The Lambda function gets run at 23:00 every day by a Cron eventbridge event.

This Repo contains the Lambda Function.

