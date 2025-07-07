<?php

require_once __DIR__ . '/vendor/autoload.php';

use App\EmailNotifier;
use App\TaskService;


$notifier = new EmailNotifier();
$taskService = new TaskService($notifier);

$task = $taskService->createTask("Finish report", "Finalize the financial report by Friday.");
