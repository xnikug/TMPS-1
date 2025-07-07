<?php
namespace Tests;

use PHPUnit\Framework\TestCase;
use App\TaskReportGenerator;
use App\TaskRepositoryInterface;
use App\Task;
use App\TaskStatus;

class TaskReportGeneratorTest extends TestCase {
    public function testGenerateStatusReport(): void {
        $task1 = new Task('Task 1', 'Description 1');
        $task2 = new Task('Task 2', 'Description 2');
        $task2->markAsCompleted();
        
        $mockRepository = $this->createMock(TaskRepositoryInterface::class);
        $mockRepository->expects($this->once())
            ->method('findAll')
            ->willReturn([$task1, $task2]);
        
        $generator = new TaskReportGenerator($mockRepository);
        $report = $generator->generateStatusReport();
        
        $this->assertStringContainsString('Task Status Report', $report);
        $this->assertStringContainsString('Pending: 1', $report);
        $this->assertStringContainsString('Completed: 1', $report);
        $this->assertStringContainsString('Total Tasks: 2', $report);
    }

    public function testGenerateOverdueReport(): void {
        $overdueTask = new Task('Overdue Task', 'Description', 'john@example.com', new \DateTime('-2 days'));
        
        $mockRepository = $this->createMock(TaskRepositoryInterface::class);
        $mockRepository->expects($this->once())
            ->method('findOverdueTasks')
            ->willReturn([$overdueTask]);
        
        $generator = new TaskReportGenerator($mockRepository);
        $report = $generator->generateOverdueReport();
        
        $this->assertStringContainsString('Overdue Tasks Report', $report);
        $this->assertStringContainsString('Overdue Task', $report);
        $this->assertStringContainsString('john@example.com', $report);
    }
}
