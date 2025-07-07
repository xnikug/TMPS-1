<?php
require_once __DIR__ . '/vendor/autoload.php';

use App\EmailNotifier;
use App\SmsNotifier;
use App\SlackNotifier;
use App\TaskService;
use App\InMemoryTaskRepository;
use App\NotificationService;
use App\TaskReportGenerator;
use App\TaskStatus;

// Create dependencies
$repository = new InMemoryTaskRepository();
$emailNotifier = new EmailNotifier('smtp.example.com', 587);
$smsNotifier = new SmsNotifier('api-key-12345');

// Create services
$taskService = new TaskService($emailNotifier, $repository);
$notificationService = new NotificationService();
$reportGenerator = new TaskReportGenerator($repository);

// Add multiple notifiers to notification service
$notificationService->addNotifier($emailNotifier);
$notificationService->addNotifier($smsNotifier);

echo "=== Task Management System Demo ===\n\n";

// Create tasks
echo "Creating tasks...\n";
$task1 = $taskService->createTask(
    "Finish report", 
    "Finalize the financial report by Friday.", 
    "john@example.com",
    new DateTime('+3 days')
);

$task2 = $taskService->createTask(
    "Update website", 
    "Update the company website with new content.", 
    "jane@example.com",
    new DateTime('-1 day') // Overdue task
);

$task3 = $taskService->createTask(
    "Team meeting", 
    "Prepare agenda for team meeting."
);

echo "\nCompleting a task...\n";
$taskService->completeTask(1);

echo "\nTesting multiple notifications...\n";
$notificationService->notifyAll($task2);

echo "\nGenerating reports...\n";
echo $reportGenerator->generateStatusReport();
echo "\n";
echo $reportGenerator->generateOverdueReport();

echo "\nGetting tasks by status...\n";
$pendingTasks = $taskService->getTasksByStatus(TaskStatus::PENDING);
echo "Pending tasks: " . count($pendingTasks) . "\n";

$overdueTasks = $taskService->getOverdueTasks();
echo "Overdue tasks: " . count($overdueTasks) . "\n";