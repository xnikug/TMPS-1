<?php
namespace Tests;

use PHPUnit\Framework\TestCase;
use App\TaskService;
use App\NotifierInterface;
use App\TaskRepositoryInterface;
use App\Task;
use App\TaskStatus;

class TaskServiceTest extends TestCase {
    private $mockNotifier;
    private $mockRepository;
    private TaskService $taskService;

    protected function setUp(): void {
        $this->mockNotifier = $this->createMock(NotifierInterface::class);
        $this->mockRepository = $this->createMock(TaskRepositoryInterface::class);
        $this->taskService = new TaskService($this->mockNotifier, $this->mockRepository);
    }

    public function testCreateTaskWithNotification(): void {
        $this->mockRepository->expects($this->once())
            ->method('save')
            ->with($this->isInstanceOf(Task::class));

        $this->mockNotifier->expects($this->once())
            ->method('send')
            ->with($this->isInstanceOf(Task::class));

        $task = $this->taskService->createTask('Test Task', 'Test Description', 'john@example.com');
        
        $this->assertEquals('Test Task', $task->title);
        $this->assertEquals('Test Description', $task->description);
        $this->assertEquals('john@example.com', $task->assignedTo);
    }

    public function testCreateTaskWithoutNotification(): void {
        $this->mockRepository->expects($this->once())
            ->method('save')
            ->with($this->isInstanceOf(Task::class));

        $this->mockNotifier->expects($this->never())
            ->method('send');

        $task = $this->taskService->createTask('Test Task', 'Test Description');
        
        $this->assertEquals('Test Task', $task->title);
        $this->assertEquals('Test Description', $task->description);
        $this->assertEquals('', $task->assignedTo);
    }

    public function testCompleteTaskSuccess(): void {
        $task = new Task('Test Task', 'Test Description');
        
        $this->mockRepository->expects($this->once())
            ->method('findById')
            ->with(1)
            ->willReturn($task);

        $this->mockRepository->expects($this->once())
            ->method('save')
            ->with($task);

        $result = $this->taskService->completeTask(1);
        
        $this->assertTrue($result);
        $this->assertEquals(TaskStatus::COMPLETED, $task->status);
    }

    public function testCompleteTaskNotFound(): void {
        $this->mockRepository->expects($this->once())
            ->method('findById')
            ->with(1)
            ->willReturn(null);

        $this->mockRepository->expects($this->never())
            ->method('save');

        $result = $this->taskService->completeTask(1);
        
        $this->assertFalse($result);
    }

    public function testGetTasksByStatus(): void {
        $tasks = [new Task('Task 1', 'Description 1'), new Task('Task 2', 'Description 2')];
        
        $this->mockRepository->expects($this->once())
            ->method('findByStatus')
            ->with(TaskStatus::PENDING)
            ->willReturn($tasks);

        $result = $this->taskService->getTasksByStatus(TaskStatus::PENDING);
        
        $this->assertEquals($tasks, $result);
    }
}