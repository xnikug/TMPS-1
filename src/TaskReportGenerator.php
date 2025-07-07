<?php
namespace App;

class TaskReportGenerator {
    private TaskRepositoryInterface $repository;

    public function __construct(TaskRepositoryInterface $repository) {
        $this->repository = $repository;
    }

    public function generateStatusReport(): string {
        $tasks = $this->repository->findAll();
        $statusCounts = [];

        foreach ($tasks as $task) {
            $status = $task->status->value;
            $statusCounts[$status] = ($statusCounts[$status] ?? 0) + 1;
        }

        $report = "Task Status Report\n";
        $report .= "==================\n";
        foreach ($statusCounts as $status => $count) {
            $report .= ucfirst($status) . ": $count\n";
        }
        $report .= "Total Tasks: " . count($tasks) . "\n";

        return $report;
    }

    public function generateOverdueReport(): string {
        $overdueTasks = $this->repository->findOverdueTasks();
        
        $report = "Overdue Tasks Report\n";
        $report .= "===================\n";
        
        if (empty($overdueTasks)) {
            $report .= "No overdue tasks found.\n";
        } else {
            foreach ($overdueTasks as $task) {
                $daysOverdue = $task->dueDate->diff(new \DateTime())->days;
                $report .= "- {$task->title} (Assigned to: {$task->assignedTo}, {$daysOverdue} days overdue)\n";
            }
        }

        return $report;
    }
}