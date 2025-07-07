<?php
namespace Tests;

use PHPUnit\Framework\TestCase;
use App\Task;
use App\TaskStatus;

class TaskTest extends TestCase {
    public function testTaskCreation(): void {
        $task = new Task('Test Task', 'Test Description', 'john@example.com');
        
        $this->assertEquals('Test Task', $task->title);
        $this->assertEquals('Test Description', $task->description);
        $this->assertEquals('john@example.com', $task->assignedTo);
        $this->assertEquals(TaskStatus::PENDING, $task->status);
        $this->assertInstanceOf(\DateTime::class, $task->createdAt);
    }

    public function testTaskStatusChange(): void {
        $task = new Task('Test Task', 'Test Description');
        
        $task->markAsInProgress();
        $this->assertEquals(TaskStatus::IN_PROGRESS, $task->status);
        
        $task->markAsCompleted();
        $this->assertEquals(TaskStatus::COMPLETED, $task->status);
    }

    public function testOverdueTask(): void {
        $pastDate = new \DateTime('-2 days');
        $task = new Task('Test Task', 'Test Description', 'john@example.com', $pastDate);
        
        $this->assertTrue($task->isOverdue());
    }

    public function testNotOverdueTask(): void {
        $futureDate = new \DateTime('+2 days');
        $task = new Task('Test Task', 'Test Description', 'john@example.com', $futureDate);
        
        $this->assertFalse($task->isOverdue());
    }

    public function testCompletedTaskNotOverdue(): void {
        $pastDate = new \DateTime('-2 days');
        $task = new Task('Test Task', 'Test Description', 'john@example.com', $pastDate);
        $task->markAsCompleted();
        
        $this->assertFalse($task->isOverdue());
    }
}