<?php
use PHPUnit\Framework\TestCase;
use App\Task;
use App\TaskService;
use App\NotifierInterface;

class TaskServiceTest extends TestCase {
    public function testTaskIsCreatedAndNotificationSent() {
        // Create mock notifier
        $mockNotifier = new class implements NotifierInterface {
            public bool $notified = false;
            public ?Task $receivedTask = null;

            public function send(Task $task): void {
                $this->notified = true;
                $this->receivedTask = $task;
            }
        };

        $service = new TaskService($mockNotifier);
        $task = $service->createTask("Write tests", "Use TDD to write this app");

        // Assertions
        $this->assertEquals("Write tests", $task->title);
        $this->assertEquals("Use TDD to write this app", $task->description);
        $this->assertTrue($mockNotifier->notified);
        $this->assertEquals($task, $mockNotifier->receivedTask);
    }
}
